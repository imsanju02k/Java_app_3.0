#!/usr/bin/env python3

import requests
import subprocess

def jfrogUpload() :
    # define the url file path, and authentication credentials and change ur IP Address
    url = 'http://<IP Address>:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    file_path = '/var/lib/jenkins/workspace/java-3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    username = 'admin'
    password = 'password' #replace 'your password with ur actual password'

    #send the PUT request with authentication and file upload
    with open(file_path, 'rb') as file:
        response = requests.put(url, auth=(username, password), data=file)
    #check the response.status code
    if response.status_code == 201:
        print("\nPUT request was successful!")
    else:
        print("PUT request failed with status code (response.status_code)")
        print("response content:")
        print(response.text)
def mvnBuild() :
    #define the Maven Command
    maven_command = "mvn clena install -DskipTests"

    #Run the maven command as a subprocess
    try:
        subprocess.run(maven_command, check=True, text=True, shell=True)
        print("/nMaven build completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Maven Build failed with exit code (e.returncode)")

def main() :
    #mvnBuild()
    jfrogUpload()

if __name__ == "__main__":
    main()
