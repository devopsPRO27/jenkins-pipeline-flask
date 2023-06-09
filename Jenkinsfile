pipeline{
    agent any
    stages{
        stage('checkout'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/devopsPRO27/jenkins-pipeline-flask']]])
            }
        }
        stage('build'){
            steps{
                sh 'echo'
            }
           
        }
        stage('test'){
            steps{
                sh 'test'
            }
           
        }
        stage('build an image'){
            steps{
                sh 'build image'
            }
           
        }  
        stage('post'){
            steps{
                sh 'psot'
            }
           
        }
    }
}
