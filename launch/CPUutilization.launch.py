# SPDX-FileCopyrightText: 2025 Hikaru Nemoto 　　　　　
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    cpuutilization = launch_ros.actions.Node(
        package='mypkg',
        executable='cpuutilization',
        )

    return launch.LaunchDescription([cpuutilization])
