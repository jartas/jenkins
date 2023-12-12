pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/jartas/jenkins.git']])
            }
        }
        stage('Test') {
            steps {
                sh 'python3 --version'
            }
        }     
        stage('Build') {
            steps {
                sh 'python3 main.py'
            }
        }           
    }
}
