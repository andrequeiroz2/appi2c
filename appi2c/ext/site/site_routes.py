from flask import Blueprint, render_template
from flask_login import login_required
from appi2c.ext.group.group_controller import (list_all_group,
                                               list_all_devices_in_group,
                                               num_group)

from appi2c.ext.device.device_controller import (num_device,
                                                 #list_device_in_goup,
                                                 list_all_device,
                                                 num_device_in_user)

from appi2c.ext.mqtt.mqtt_controller import num_broker

from appi2c.ext.auth.auth_controller import num_user

from flask_login import current_user


bp = Blueprint('site', __name__)


@bp.route("/")
@bp.route("/index")
def index():
    if current_user.is_authenticated:
        user = current_user.username
        groups = list_all_group(current_user)
        total_device = num_device_in_user(current_user)
        return render_template("index.html",
                               user=user,
                               total_device=total_device,
                               groups=groups
                               )
    else:
        total_user = num_user()
        total_device = num_device()
        total_group = num_group()
        total_broker = num_broker()
    return render_template("index.html",
                           total_device=total_device,
                           total_user=total_user,
                           total_group=total_group,
                           total_broker=total_broker)