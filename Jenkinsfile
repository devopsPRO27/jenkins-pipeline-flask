pipeline{
    agent {
        docker{
            image 'python'
            args '-p 5000:5000 -u root'
        }
    parameters{
        string(name:'NAME',defaultValue:'',description:'omername')
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
                sh 'pip3 install -r requirements.txt'
                sh 'python3 main.py &'
            }
           
        }
        stage('test'){
            steps{
                sh 'pytest test.py'
            }
           
        }
        stage('build an image'){
            when{
                branch 'dev'
            }

            steps{
                sh 'echo build image'
            }
           
        }  
        stage('post'){
            steps{
                echo "post $params.NAME"
            }
           
        }
    }
}
