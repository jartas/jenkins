pipeline {
	agent none
  stages {
  	stage('Maven Install') {
    	agent {
      	docker {
        	image 'redis'
        }
      }
    }
    stage('Docker Build') {
    	agent any
      steps {
      	sh 'docker build -t redis/redis-stack .'
      }
    }
  }
}
