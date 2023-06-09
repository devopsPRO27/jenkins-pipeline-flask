pipeline{
    agent {
        docker{
            image 'python'
            args '-p 5000:5000'
        }
    }
    stages{
        stage('checkout'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/devopsPRO27/jenkins-pipeline-flask']]])
            }
        }
        stage('build'){
            steps{
                sh 'sudo pip3 install -r requirements.txt'
                sh 'python3 main.py'
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
