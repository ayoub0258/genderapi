// Infra as code
//

provider "google" {
  project     = "ensai-2025"
  region      = "europe-west1"
  zone        = "europe-west1-b"
  credentials = "../ensai-2025-8f3e0d316c90.json"
}

resource google_compute_instance "test-christophe" {
    name         = "test-christophe"
    machine_type = "f1-micro"
    zone         = "europe-west1-b"

    boot_disk {
        initialize_params {
        image = "debian-cloud/debian-11"
        }
    }

    network_interface {
        network = "default"

        access_config {
        // Ephemeral public IP
      }
    }

    tags = ["http-server"]

    metadata_startup_script = "echo Bonjour > index.html && sudo python3 -m http.server 80 &"
}