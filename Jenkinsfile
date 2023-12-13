pipeline {
    agent none
    stages {
        stage('Build') { 
            steps {
                sh 'sleep 15' 
            }
        }
        stage('Docker') { 
            agent {
                docker {image 'python:latest'}
            }
            steps {
                sh 'python3 version' 
            }
        }
    }
}
