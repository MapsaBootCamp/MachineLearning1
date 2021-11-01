import cv2
import glob
import matplotlib.pyplot as plt
import imutils
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.decomposition import PCA, KernelPCA
from sklearn.ensemble import RandomForestClassifier


model =  SVC(kernel='linear')
ext = ['jpg', 'JPG', 'pnp', 'jpeg']


def get_files(path_, ext):
    temp_paths = []
    [temp_paths.extend(glob.glob(path_ + '*.' + e)) for e in ext]
    return temp_paths

files_yes = get_files('data/yes/', ext)
files_no = get_files('data/no/', ext)


def read_files(files):
    temp_images = []
    for file in files:
        temp_img = cv2.imread(file)
        if temp_img is not None:
            temp_images.append(cv2.imread(file))
    return temp_images

tumor_imgs_yes = read_files(files_yes)
tumor_imgs_no = read_files(files_no)


def crop_brain(image):
    
    # Convert the image to grayscale, and blur it slightly
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    
    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours in thresholded image, then grab the largest one
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)
    # extreme points
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])
    
    # crop new image out of the original image using the four extreme points (left, right, top, bottom)
    new_image = image[extTop[1]:extBot[1], extLeft[0]:extRight[0]]            
    
    return new_image


tumor_imgs_croped_yes = []
tumor_imgs_croped_no = []



for image in tumor_imgs_yes:
    x = crop_brain(image)
    x_resize = cv2.resize(x, (128, 128))
    gray = cv2.cvtColor(x_resize, cv2.COLOR_BGR2GRAY)
    tumor_imgs_croped_yes.append(gray)


for image in tumor_imgs_no:
    x = crop_brain(image)
    x_resize = cv2.resize(x, (128, 128))
    gray = cv2.cvtColor(x_resize, cv2.COLOR_BGR2GRAY)
    tumor_imgs_croped_no.append(gray)


y_yes = np.ones(len(tumor_imgs_croped_yes), dtype="int8")
y_no = np.zeros(len(tumor_imgs_croped_no), dtype="int8")



X = np.concatenate((tumor_imgs_croped_yes, tumor_imgs_croped_no), axis=0)
y = np.concatenate((y_yes, y_no), axis=0)

d1, d2, d3 = X.shape

X = X.reshape((d1, d2 * d3))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)


# scale data before train model
scaler_ = StandardScaler()
X_train_sc = scaler_.fit_transform(X_train)
X_test_sc = scaler_.transform(X_test)


# random forest without pca
rf_model = RandomForestClassifier()
rf_model.fit(X_train_sc, y_train)
y_predict_rf = rf_model.predict(X_test_sc)


# SVC without pca
svc_model = SVC(kernel="linear")
svc_model.fit(X_train_sc, y_train)
y_predict_svc = svc_model.predict(X_test_sc)

# PCA
data_pca = PCA(n_components=12)
pca_components = data_pca.fit(X_train_sc)
X_train_pca = pca_components.fit_transform(X_train_sc)
X_test_pca = pca_components.transform(X_test_sc)

# KernelPCA
data_kpca = KernelPCA()
kpca_components = data_kpca.fit(X_train_sc)
X_train_kpca = kpca_components.fit_transform(X_train_sc)
X_test_kpca = kpca_components.transform(X_test_sc)


# RandomForest With PCA
rf_model_pca = RandomForestClassifier()
rf_model_pca.fit(X_train_pca, y_train)
y_predict_rf_pca = rf_model_pca.predict(X_test_pca)

# SVC With PCA
svc_model_pca = SVC(kernel="linear")
svc_model.fit(X_train_pca, y_train)
y_predict_pca = svc_model.predict(X_test_pca)


# RandomForest With KernelPCA
rf_model_kpca = RandomForestClassifier()
rf_model_kpca.fit(X_train_kpca, y_train)
y_predict_rf_kpca = rf_model_kpca.predict(X_test_kpca)

# SVC With KernelPCA
svc_model_kpca = SVC(kernel="linear")
svc_model.fit(X_train_kpca, y_train)
y_predict_kpca = svc_model.predict(X_test_kpca)


print("without PCA: ", accuracy_score(y_test, y_predict_svc))
print("with PCA: ", accuracy_score(y_test, y_predict_pca))

print("without PCA:")
print(classification_report(y_test, y_predict_svc))
print("with PCA:")
print(classification_report(y_test, y_predict_pca))


print("RandomForest without PCA:")
print(classification_report(y_test, y_predict_rf))

print("RandomForest with PCA:")
print(classification_report(y_test, y_predict_rf_pca))


print("RandomForest without KPCA:")
print(classification_report(y_test, y_predict_rf_kpca))

print("SVC with KPCA:")
print(classification_report(y_test, y_predict_kpca))

