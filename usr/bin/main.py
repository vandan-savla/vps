import os
import argparse

def configure_web_server():
    # Install Apache web server (assuming you're using a Debian-based system)
    # os.system("sudo apt-get update")
    os.system("sudo apt-get install apache2 -y")

    # Configure a virtual host
    virtual_host_config = """
    <VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>
    """
    site_name = input("Enter Your Site Name: ")
    os.system(f"sudo mkdir /etc/apache2/sites-available/{site_name}.conf")
    
    with open(f"/etc/apache2/sites-available/{site_name}.conf", "w") as f:
        f.write(virtual_host_config)

    # Enable the virtual host
    os.system(f"sudo a2ensite {site_name}.conf")

    # Restart Apache to apply changes
    os.system("sudo systemctl restart apache2")
    
    print("Successfully Configured the Apache2 WebServer")


def configure_database_server():
    # Install MySQL server (assuming you're using a Debian-based system)
    # os.system("sudo apt-get update")
    os.system("sudo apt-get install mysql-server -y")

    # Secure MySQL installation
    os.system("sudo mysql_secure_installation -y")

    # Create a database and user (replace 'yourdb' and 'youruser' with your values)
    db=input("Enter The Database Name: ")
    username=input("Enter The Username: ")
    passwd=input("Enter Password: ")
    os.system(f"sudo mysql -e 'CREATE DATABASE {db};'")
    os.system(f"sudo mysql -e 'CREATE USER {username}@localhost IDENTIFIED BY {passwd};'")
    os.system(f"sudo mysql -e 'GRANT ALL PRIVILEGES ON {db}.* TO {username}@localhost;'")
    os.system(f"sudo mysql -e 'FLUSH PRIVILEGES;'")
    
    print("Successfully Configured the MySql Server")


def configure_security():
    # Configure firewall (e.g., ufw)
    try:
        os.system("sudo apt-get install ufw -y")
        os.system("sudo ufw allow OpenSSH")
        os.system("sudo ufw enable")

        # Install and configure Fail2ban (intrusion prevention)
        os.system("sudo apt-get install fail2ban -y")
        os.system("sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local")
        os.system("sudo systemctl start fail2ban")
        os.system("sudo systemctl enable fail2ban")

        # Set up automatic security updates
        os.system("sudo apt-get install unattended-upgrades")
        auto_updates_config = """
        APT::Periodic::Update-Package-Lists "1";
        APT::Periodic::Download-Upgradeable-Packages "1";
        APT::Periodic::AutocleanInterval "7";
        APT::Periodic::Unattended-Upgrade "1";
        """
        
        with open("/etc/apt/apt.conf.d/10periodic", "w") as f:
            f.write(auto_updates_config)

        os.system("sudo systemctl enable unattended-upgrades")
        os.system("sudo systemctl start unattended-upgrades")
        
        print("Successfully Implemented the Firewall Settings")
    
    except Exception:
        print("Error Occured Can't implement the settings. Please Try again")
    
        
def main():
    parser = argparse.ArgumentParser(description="VPS Configuration and Security Tool")
    parser.add_argument("--web-server", action="store_true", help="Configure web server")
    parser.add_argument("--database-server", action="store_true", help="Configure database server")
    parser.add_argument("--security", action="store_true", help="Implement security measures")
    
    args = parser.parse_args()

    if args.web_server:
        print("Configuring Web Server...")
        configure_web_server()

    if args.database_server:
        print("Configuring Database Server...")
        configure_database_server()

    if args.security:
        print("Implementing Security Measures...")
        configure_security()

    print("Configuration and security setup complete.")

if __name__ == "__main__":
    main()
