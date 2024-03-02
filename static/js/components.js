
function LogoHead() {
  return (
      <a href="/" class="nav-link px-2 link-secondary" >
        <img src="../static/images/Dapper.gif" />
      </a>
  );
}

// Using a class component 
class HeaderBar extends React.Component {
  render() { return (<header class="" id="main_header">
              <div class="container">
                <div class="row">
                  <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start col-6 col-md-3 col-sm-4">
                      <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
                          <li>
                              <LogoHead />
                          </li>
                      </ul>
                  </div>
                  <div class="col-1 col-md-6 col-sm-4">
                  </div>
                  <div class="col-5 col-md-3 col-sm-4 text-left">
                  </div>
                </div>
              </div>
          </header>
    );
  }
}


// Using a functional component
function FooterBar() {
  return ( <footer class="footer mt-auto py-3 bg-light">
            <div class="container">
                <a href="#main_header">Back to top</a>
            </div>
          </footer>);
}


// headerBar does not work the first letter to be capitalize
ReactDOM.render(<HeaderBar />, document.getElementById('header'));
ReactDOM.render(<FooterBar />, document.getElementById('footer'));

