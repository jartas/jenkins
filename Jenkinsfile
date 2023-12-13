pipeline {
    agent any
    stages {
        stage('Start database') { 
            agent {
                docker.image('redis:3.0.7-alpine').withRun { c ->
                    def ip = hostIp(c)
                    
                    stage 'client set'
                    
                    docker.image('redis:3.0.7-alpine').inside {
                        sh "redis-cli -h ${ip} set test 123"
                    }
            }

        }
    }
}
