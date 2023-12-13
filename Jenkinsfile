pipeline {
    agent any
    stages {
        stage('Docker') { 
            agent {
                docker {image 'python:latest'}
            }
            steps {
                sh 'python3 --version' 
            }
        }
    }
}
