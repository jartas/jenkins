pipeline {
    agent any
    stages {
        stage('Docker') { 
            agent {
                docker {image 'redis'}
            }
            steps {
                sh 'python3 version' 
                sh 'python3 --version' 
            }
        }
    }
}
