pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                my-docker {
                    image 'python:3.12.1-alpine3.19' 
                }
            }
            steps {
                sh 'python3 main.py' 
            }
        }
    }
}
