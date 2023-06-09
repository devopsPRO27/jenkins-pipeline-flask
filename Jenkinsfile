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
                sh 'echo test'
            }
           
        }
        stage('build an image'){
            steps{
                sh 'echo build image'
            }
           
        }  
        stage('post'){
            steps{
                echo 'post'
            }
           
        }
    }
}
