################################################################
# CentOS Default Bash Configuration
################################################################
if [ -f /etc/bashrc ]; then
  . /etc/bashrc
fi

################################################################
# Vagrant Custom Bash Configuration
################################################################
export DJANGO_SETTINGS_MODULE="vanilla.settings.development"
cd /application/
