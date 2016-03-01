#! /bin/sh
# /etc/init.d/detector-init
 
### BEGIN INIT INFO
# Provides:          detector-init
# Required-Start:    $all
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Script de ejemplo de arranque automático
# Description:       Script para arrancar el detector de presencia
### END INIT INFO
 
 
# Dependiendo de los parámetros que se le pasen al programa se usa una opción u otra
case "$1" in
  start)
    echo "Arrancando suma_puntos-init"
    # Aquí hay que poner el programa que quieras arrancar automáticamente
    /usr/bin/python /home/pi/Repos/RFID-MiCity/suma_puntos.py
    ;;
  stop)
    echo "Deteniendo suma_puntos-init"
 
    ;;
  *)
    echo "Modo de uso: /etc/init.d/suma_puntos-init {start|stop}"
    exit 1
    ;;
esac
 
exit 0
