pipeline {
    agent { dockerfile true }
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/jartas/jenkins.git']])
            }
        }
        stage('Test') {
            steps {
                sh 'node --version'
                sh 'svn --version'
            }
        }        
    }
}
