pipeline {
    agent any
    stages {
        stage("Login to Docker hub"){
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    bat "docker login -u $USERNAME -p $PASSWORD"
                }    
            }
        }
        stage('Building and unit testing'){
            steps {
                bat "git checkout ${env.GIT_BRANCH}"
                dir('backend_rating') {
                    bat 'pip install -r requirements.txt'
                    bat "python -m unittest"
                }
                dir('frontend_rating') {
                    bat 'pip install -r requirements.txt'
                    bat "pytest -s test_mLOPSfronttest.py"
                }
            }
        }
        stage('Push to Develop') {
            steps {
                bat 'git checkout dev'
                bat 'git pull'
                bat "git merge ${env.GIT_BRANCH}"
                bat 'git push origin dev'
                bat 'git remote prune origin'
            }
        }
        stage('User Acceptance') {
            input {
                message "Proceed to push to main"
                ok "Yes"
            }
            steps {
                bat 'git checkout main'
                bat 'git pull'
                bat 'git merge dev'
                bat 'git push origin main'
            }
        }
        stage('Pushing to Dockerhub') {
            steps {
                bat 'docker-compose up --build -d'
                bat 'docker push wvaihau/api-prediction-image:latest'
                bat 'docker push wvaihau/frontend-prediction-image:latest'
            }
        }
    }
    post {
        always {
            bat 'docker logout'
        }
    }
}
