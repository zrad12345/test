pipeline {
  agent any
  triggers { 
    pollSCM("*/1 * * * *")
  }
  stages {
    stage("Run tests") {
      steps {
       sh "python test_calculator.py"
      }
    }
  }
}
