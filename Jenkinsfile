pipeline {
    agent {
        docker {image 'python:latest'}
    }
    stages {
        stage('Build') { 
            steps {
                sh 'python3 version' 
            }
        }
    }
}
