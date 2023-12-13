pipeline {
    agent any
    stages {
        stage('Docker') { 
            agent {
                docker {image 'python:latest'}
                sh 'sleep 20'
            }
            steps {
                sh 'python3 version' 
            }
        }
    }
}
