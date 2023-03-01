class Footer extends HTMLElement {
    constructor() {
      super();
    }
  
    connectedCallback() {
      this.innerHTML = `
        <style>

        </style>
        <footer class="footer mt-auto py-3 bg-light">
            <div class="container">
                <a href="#main_header">Back to top</a>
            </div>
        </footer>
      `;
    }
  }
  
  customElements.define('footer-component', Footer);