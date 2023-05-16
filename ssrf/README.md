# Server Side Request Forgery (SSRF)
This will include the demo files used in my youtube video on ssrf.

### How to run 
1. Ensure you have docker installed and running 
2. Clone the repo
 	`git clone xxx`
2. Navigate to repo directory and build image
    `docker build -t owasp-ssrf .`
3. Run the image in a docker container
 	`docker run -d -p 5000:5000 owasp-ssrf`
4. Navigate to  `http://127.0.0.1`

### How to stop and remove container and image
1. Find container id
`docker ps` (find container id for owasp-ssrf)
2. Stop docker container
`docker stop <container id>`
3. Remove container
`docker rm <container id>`
4. Remove image
`docker rmi owasp-ssrf`
