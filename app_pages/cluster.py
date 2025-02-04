import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport
from scipy import stats
from feature_engine.encoding import OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from streamlit_data_management import load_pkl_file


sns.set_style('dark')

def cluster_body():

    # load cluster analysis files and pipeline
    version = 'v1'
    
    try:
        cluster_elbow = plt.imread(
            f"outputs/pictures/{version}/elbow_method.png")
        cluster_silhouette = plt.imread(
            f"outputs/pictures/{version}/silhouette_score.png")
        best_features = plt.imread(
            f"outputs/pictures/{version}/best_features.png")
        cluster_profile = pd.read_csv(
            f"outputs/datasets/other/{version}/clusters_profile.csv")
    except FileNotFoundError as e:
        st.error(f"Error loading files: {e}")
        return


    st.write("## ML Cluster")

    st.info(
        f"* We modeled a cluster pipeline. \n"
        f"* We used **Principal Component Analysis (PCA)** to determine the best features to train the model with. \n"
        f"* We dertermine the number of cluster needed with Elbow and Silhouette methode\n"
        f"* Finally we profiled the cluster"
    )

    st.write("#### The most important features")
    st.image(best_features)

    st.write("#### Clusters Elbow Plot")
    st.image(cluster_elbow)

    st.write("#### Clusters Silhouette Plot")
    st.image(cluster_silhouette)
        
    st.write("#### Clusters Profiling")
    cluster_profile.index = [" "] * len(cluster_profile)
    st.table(cluster_profile)