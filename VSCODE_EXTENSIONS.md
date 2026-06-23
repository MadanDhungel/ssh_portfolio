## VS Code Extensions Recommended

To get the best experience with this project, install these extensions:

### Essential for Helm
- **Helm for Visual Studio Code** (`ms-kubernetes-tools.vscode-helm`)
  - Provides language support for Helm charts
  - Fixes red line issues in template files
  - Syntax highlighting for Helm templates

### Kubernetes & Docker
- **Kubernetes** (`ms-kubernetes-tools.vscode-kubernetes-tools`)
  - Full Kubernetes support in VS Code
  - Deploy and manage resources from editor

- **Docker** (`ms-azuretools.vscode-docker`)
  - Docker image and container support
  - Docker Compose support

### YAML & Code Quality
- **YAML** (`redhat.vscode-yaml`)
  - Better YAML validation and completion
  - Kubernetes schema support

- **Prettier** (`esbenp.prettier-vscode`)
  - Code formatting for YAML and JSON

### Optional but Useful
- **Makefile Tools** (`ms-vscode.makefile-tools`)
  - If using Makefiles for automation

### Installation

You can install all recommended extensions with:
```bash
# Open command palette (Ctrl+Shift+P / Cmd+Shift+P)
# Type: Extensions: Show Recommended Extensions
# Or use the Extensions panel sidebar
```

Alternatively, install manually:
```bash
code --install-extension ms-kubernetes-tools.vscode-helm
code --install-extension ms-kubernetes-tools.vscode-kubernetes-tools
code --install-extension ms-azuretools.vscode-docker
code --install-extension redhat.vscode-yaml
code --install-extension esbenp.prettier-vscode
```
