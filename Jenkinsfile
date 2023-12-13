pipeline {
    agent {
        docker {images 'python:latest'}
    }
    stages {
        stage('Build') { 
            steps {
                sh 'python3 version' 
            }
        }
    }
}
