#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Tikyo
# @Datetime : 2020-04-26 09:26


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user_id': user.id,
        'user_name': user.user_name
    }

