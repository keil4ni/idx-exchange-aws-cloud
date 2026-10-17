### Lab 3.1
The second step of the handbook says to create an EC2 instance using an Amazon Linux 2023 AMI which uses an "image" of a template needed to provide the software for the instance. I used a t3.micro instance type to stay in the Free tier for AWS usage since it provides enough to setup the PropertyLite app. We also create a corresponding key-pair in RSA and pem format as a form of security for connecting to our instance, and we name it ``training-key``.

When configuring our instance, we made sure to create a security group with inbound rules where we can SSH into the instance through our IP and we also have a custom TCP port 8080 that can be accessed through any IP. In the user details, we attached the bootstrap script that runs to install Python and Flask along with the ``app.py`` code from Week 0, all which are needed to run the PropertyLite app.

Afterward, we launch the instance and wait for all status checks to pass before SSH-ing into it and we make sure to get the Public IPv4 address in order to test the curl checks.

### Lab 3.2
After confirming the instance is running, we create a snapshot of this EC2 instance which saves it as a backup of the data from an EBS volume. Having a snapshot of our data allows us to restore volumes if needed, which makes the data highly available, but it's important to note that the snapshots do not account for live updates.