# install & configure nginx server with puppet

$config = "server {
	listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html;

        location /redirect_me {
                return 301 https://www.linkedin.com/in/zakaria-rdouane-190a93242/;
        }
}"

package { 'nginx':  # install nginx server
ensure	=> 'installed',
}

file { 'index.html':
ensure	=> 'present',
path	=> '/var/www/html/index.html',
content	=> 'Hello World!',
mode	=> '0644'
}

file { 'server_config':
ensure	=> 'present',
path 	=> '/etc/nginx/sites-available/default',
content => $config
}

exec { 'service nginx restart':
path	=> ['/usr/sbin', '/usr/bin']
}
