pipeline{
    agent any

    environment{
        NEXUS_ADDRESS = 'localhost:8083'
        IMAGE = 'capstone_blogsite'
        TAG = '1.0'
        DEPLOYED_CONTAINER = 'containerized_blogsite'
        PROD_IP_ADD = '192.168.56.102'
        CONTAINER_IP = '172.18.0.3'
        CONTAINER_PORT = '8008'
        APP_PORT= '3000'
        TAR_FILE='blogsite.tar'
    }

    stages{
        stage('Build Step'){
            steps {
                sh "npm install"

                //Dockerization
                sh "docker build -t $IMAGE ."
                //Adding tags to image
                sh "docker tag $IMAGE $NEXUS_ADDRESS/$IMAGE:$TAG"
                //Running container and Docker cleanup
                
                sh '''
                if [ $(docker ps -a -f name=\$DEPLOYED_CONTAINER | grep -o \$DEPLOYED_CONTAINER) ]; then docker stop \$DEPLOYED_CONTAINER; docker rm \$DEPLOYED_CONTAINER; fi
                docker run -d -p \$CONTAINER_PORT:\$APP_PORT --restart unless-stopped --net mynetwork --ip \$CONTAINER_IP --name \$DEPLOYED_CONTAINER \$NEXUS_ADDRESS/\$IMAGE:\$TAG
                docker system prune -f
                '''
            }
        }
        stage('Testing'){
            steps{
                echo "-------- Test Phase Started :: Integration Testing via Automated Scripts :: --------"
                sh "npm test"
                echo "-------- Test Phase Finished :: Integration Testing via Automated Scripts :: --------"
            }
        }
        stage('Artifact Archiving'){
            steps{
                echo ""
                echo "---------- Provisioning Phase Started :: Deploying Artifacts to Nexus Repository :: ----------"

                //Login to the Docker repository
                withCredentials([usernamePassword(credentialsId: 'nexus', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                sh "docker login -u $USERNAME -p $PASSWORD $NEXUS_ADDRESS"
                }

                //Artifact deployment
                echo ""
                echo "---------- Integration Phase Started :: Deploying Artifacts :: ----------"
                sh "docker push $NEXUS_ADDRESS/$IMAGE:$TAG"
            }
        }
        
        stage("Deployment"){
            steps{
                //Prepare container to be deployed.
                sh "docker save $NEXUS_ADDRESS/$IMAGE > ./ignore-this/\$TAR_FILE"
                
                //Stops the build container
                sh '''
                docker stop \$DEPLOYED_CONTAINER
                docker rm \$DEPLOYED_CONTAINER
                '''

                //Publish image to ftp server
                withCredentials([usernamePassword(credentialsId: 'ftp', passwordVariable: 'ftp_pass', usernameVariable: 'ftp_user')]) {
                    sh ''' 
                        lftp -u \$ftp_user,\$ftp_pass -e \"cd /files; put ./ignore-this/\$TAR_FILE;quit\" \$PROD_IP_ADD
                    '''
                }
                //Stop existing deployed container and run the deployed image
                sshagent(credentials: ['production_ssh']) {
                sh '''
                    [ -d ~/.ssh ] || mkdir ~/.ssh && chmod 0700 ~/.ssh
                    ssh-keyscan -t rsa,dsa \$PROD_IP_ADD >> ~/.ssh/known_hosts
                    ssh -tt caikit@\$PROD_IP_ADD 'if [ $(docker ps -a -f name=containerized_blogsite | grep -o containerized_blogsite) ]; then docker stop containerized_blogsite; docker rm containerized_blogsite; fi; docker load < /home/caikit/ftp/files/blogsite.tar; docker run -d -p 8008:3000 --restart unless-stopped --net mynetwork --ip 172.18.0.3 --name containerized_blogsite localhost:8083/capstone_blogsite:1.0; docker system prune -af'
                '''
                }

                //Finished
                echo ""
                echo "------------------------------------------------------------"
                echo "Deployed here: http://$PROD_IP_ADD:$CONTAINER_PORT"


            }
        }
    }
}
