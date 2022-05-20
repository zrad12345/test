pipeline {
  agent {
    label "docker-agent"
  }
  triggers { 
    pollSCM("*/1 * * * *")
  }
  stages {
    stage("Build Docker image") {
      steps {
       sh "docker build -t calculator ."
      }
    }
    stage("Run tests") {
      steps {
       sh "docker run --rm calculator" 
      } 
    }
  }
}
