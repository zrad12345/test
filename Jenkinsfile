pipeline {
  agent any
  triggers { 
    posllSCM("*/1 * * * *")
  }
  stages {
    stage("Run tests") {
      steps {
       sh "python test_calculator.py"
      }
    }
  }
}
