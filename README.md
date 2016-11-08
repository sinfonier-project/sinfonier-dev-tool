# sinfonier-dev-tool
Tool to build modules for Sinfonier project.

## What do you will need to install?
* Python
* Python module "APScheduler"
* JDK
* Maven


## How to test your module?

    1. Rename YourBolt/YourSpout/YourDrain class to your class name, depending on your module target.
    2. Code your module according to the template.
    3. Set your input tuple json in src/main/resources/input.json file or use tweet default.
    4.  Code your test.  Execute Runner (in terminal, run "mvn package" in root directory of project -where "pom.xml" is-) and retrieve result tuple. Write your asserts.
    5. Your module is ready to be uploaded to Sinfonier Project.

## Virtual Machine

[Download virtual machine](https://goo.gl/owpyr4)
