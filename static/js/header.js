class Header extends HTMLElement {
    constructor() {
      super();
    }
  
    connectedCallback() {
      this.innerHTML = `
        <style>
        .b-example-divider {
            height: 3rem;
            background-color: rgba(0, 0, 0, .1);
            border: solid rgba(0, 0, 0, .15);
            border-width: 1px 0;
            box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
          }
          
          .form-control-dark {
            color: #fff;
            background-color: var(--bs-dark);
            border-color: var(--bs-gray);
          }
          .form-control-dark:focus {
            color: #fff;
            background-color: var(--bs-dark);
            border-color: #fff;
            box-shadow: 0 0 0 .25rem rgba(255, 255, 255, .25);
          }
          
          .bi {
            vertical-align: -.125em;
            fill: currentColor;
          }
          
          .text-small {
            font-size: 85%;
          }
          
          .dropdown-toggle {
            outline: 0;
          }
          
        </style>
        <header class="p-3 mb-3 border-bottom">
            <div class="container">
              <div class="row">
                <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start col-3">
                    <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
                        <li><a href="/" class="nav-link px-2 link-secondary" ><img src="../static/images/Dapper.gif" ></a></li>
                    </ul>
                </div>
                <div class="col-6">
                </div>
                <div class="col-3">
                  <a href="/create" class="nav-link px-2 link-secondary">Create Article</a>
                </div>
              </div>
            </div>
        </header>
    
      `;
    }
  }
  
  customElements.define('header-component', Header);