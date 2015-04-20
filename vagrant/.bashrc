################################################################
# CentOS Default Bash Configuration
################################################################
if [ -f /etc/bashrc ]; then
  . /etc/bashrc
fi

################################################################
# Vagrant Custom Bash Configuration
################################################################

# Vagrant terminal color
export PS1="\[\e[00;37m\]\n\[\e[0m\]\[\e[01;35m\]\u@\h\[\e[0m\]\[\e[00;37m\] \\
\[\e[0m\]\[\e[01;34m\]\W\[\e[0m\]\[\e[00;37m\] \\$ \[\e[0m\]"

# Set Django settings
export DJANGO_SETTINGS_MODULE="vanilla.settings.development"

# Set default ssh path
cd /application/
