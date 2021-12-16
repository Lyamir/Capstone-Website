pipeline{
    agent any

    environment{
        NEXUS_ADDRESS = 'localhost:8083'
        IMAGE = 'capstone_blogsite'
        TAG = '1.0'
        CONTAINER = 'containerized_capstone_blogsite'
        DEPLOYED_CONTAINER = 'containerized_blogsite'
        PROD_IP_ADD = '192.168.56.102'
    }

    stages{
        stage('Build Step'){
            steps {
                //Dockerization
                sh "docker build -t $IMAGE:$TAG ."
                //Adding tags to image
                sh "docker tag $IMAGE:$TAG $NEXUS_ADDRESS/$IMAGE:$TAG"
                //Running container and Docker cleanup
                sh '''
                docker stop \$DEPLOYED_CONTAINER
                docker rm \$DEPLOYED_CONTAINER
                docker run -d -p 8008:3000 --restart unless-stopped --net mynetwork --ip 172.18.0.3 --name \$DEPLOYED_CONTAINER \$NEXUS_ADDRESS/\$IMAGE:\$TAG
                docker system prune
                '''
            }
        }
        stage('Testing'){
            steps{
                sh "npm i selenium-webdriver"
                echo "-------- Test Phase Started :: Integration Testing via Automated Scripts :: --------"
                sh "node test"
                echo "-------- Test Phase Finished :: Integration Testing via Automated Scripts :: --------"
            }
        }
        stage('Artifact Archiving'){
            steps{
                echo ""
                echo "---------- Provisioning Phase Started :: Deploying Artifacts to Nexus Repository :: ----------"

                withCredentials([usernamePassword(credentialsId: 'nexus', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                sh "docker login -u $USERNAME -p $PASSWORD $NEXUS_ADDRESS"
                }

                //Artifact deployment
                echo ""
                echo "---------- Integration Phase Started :: Deploying Artifacts :: ----------"
                sh "docker push $NEXUS_ADDRESS/$IMAGE:$TAG"

                //Prepare container to be deployed. Uncomment during testing
                //sh "docker save $NEXUS_ADDRESS/$IMAGE > ./ignore-this/blogsite.tar"
            }
        }
        //Uncommented during testing
        // stage("Deployment"){
        //     steps{
        //         //Publish image to ftp server
        //         withCredentials([usernamePassword(credentialsId: 'ftp', passwordVariable: 'ftp_pass', usernameVariable: 'ftp_user')]) {
        //             sh ''' 
        //                 lftp -u \$ftp_user,\$ftp_pass -e \"cd /files; put ./ignore-this/blogsite.tar;quit\" \$PROD_IP_ADD
        //             '''
        //         }
        //         //Stop existing deployed container and run the deployed image
        //         sshagent(credentials: ['production_ssh']) {
        //         sh '''
        //             [ -d ~/.ssh ] || mkdir ~/.ssh && chmod 0700 ~/.ssh
        //             ssh-keyscan -t rsa,dsa 192.168.56.102 >> ~/.ssh/known_hosts
        //             ssh -tt caikit@192.168.56.102 'docker stop containerized_blogsite; docker rm containerized_blogsite; docker load < /home/caikit/ftp/files/blogsite.tar; docker run -d -p 8008:3000 --restart unless-stopped --net mynetwork --ip 172.18.0.3 --name containerized_blogsite localhost:8083/capstone_blogsite:1.0; docker rmi -f $(docker images -f "dangling=true" -q)'
        //         '''
        //         }

        //             // docker load < home/caikit/ftp/files/blogsite.tar
        //             // docker stop \$DEPLOYED_CONTAINER
        //             // docker rm \$DEPLOYED_CONTAINER
        //             // docker run -d -p 8008:3000 --restart unless-stopped --net mynetwork --ip 172.18.0.3 --name \$DEPLOYED_CONTAINER \$NEXUS_ADDRESS/\$IMAGE:\$TAG

        //         // docker stop \$DEPLOYED_CONTAINER
        //         // docker rm \$DEPLOYED_CONTAINER


        //         // sshagent(credentials: ['production_ssh']) {
        //         // sh '''
        //         //     [ -d ~/.ssh ] || mkdir ~/.ssh && chmod 0700 ~/.ssh
        //         //     ssh-keyscan -t rsa,dsa 192.168.56.102 >> ~/.ssh/known_hosts
        //         //     ssh caikit@192.168.56.102
        //         //     ls -a
                    
        //         // '''
        //         // }


        //         // script{
        //         //     def result = sh(
        //         //         script:'docker ps -a -f name=$CONTAINER | grep -o $CONTAINER',
        //         //         returnStdout: true
        //         //     ).trim()
        //         //     if (CONTAINER.trim().equals(result)){
        //         //     echo"Removing existing containers"
        //         //     sh "docker stop $CONTAINER"
        //         //     sh "docker rm $CONTAINER"
        //         //     }
        //         // }
                
        //         // echo ""
        //         // echo "---------- Deployment Phase Started :: Building Docker Container :: ----------"
        //         // sh "docker run -d -p 8008:3000 --restart unless-stopped --net mynetwork --ip 172.18.0.3 --name $CONTAINER $IMAGE:$TAG"

        //         // //Finished
        //         // echo ""
        //         // echo "------------------------------------------------------------"
        //         // echo "Deployed here: http://localhost:8008"


        //     }
        //}
    }
}
