# Create AMI (Amazon Machine Image)

1. From AWS, search for AMI
2. Click on EC2 image builder
3. Click on Image pipeline
    - Enter name and description
    - For build schedule, select schedule builder and set time
    - Set tag (Image: Webserver)
    - Click New Recipe
    - Select AMI
    - Set Name and version (Webserver, 1.0.0)
    - Source Image, select Ubuntu
        - Quick Start
        - ARN 
        - Latest version
        - Working directory (/tmp)
        - Build components
        - Test Components (Rebooting)
        - Volume
    - Infrastructure Config
        - Choose defaults
    - Distribution Settings
        - Choose defaults
    - Review and Create

Find images in `https://console.aws.amazon.com/imagebuilder/home?region=us-east-1#/images`