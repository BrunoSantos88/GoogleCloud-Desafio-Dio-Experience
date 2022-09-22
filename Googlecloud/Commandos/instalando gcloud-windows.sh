#instalando gcloud windows

1---- passo 

#instalador gcloud#

(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")

& $env:Temp\GoogleCloudSDKInstaller.exe

2-- passo

Set-ExecutionPolicy RemoteSigned

3-- passo 

#Componets gcloud Gke#

#https://cloud.google.com/blog/products/containers-kubernetes/kubectl-auth-changes-in-gke

gcloud components install gke-gcloud-auth-plugin