pipeline {
  agent any
  triggers { 
    pollSCM("*/1 * * * *")
  }
  stages {
    stage("Run tests") {
      steps {
       sh "python3.9 test_calculator.py"
      }
    }
  }
}
