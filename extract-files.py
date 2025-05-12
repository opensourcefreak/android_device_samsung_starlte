#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2025 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
    lib_fixup_remove,
)

namespace_imports = [
    'vendor/samsung/exynos9810-common',
    'device/samsung/exynos9810-common',
]

blob_fixups: blob_fixups_user_type = {
    'vendor/lib/hw/audio.primary.exynos9810.so': blob_fixup()
        .replace_needed('libvndsecril-client.so', 'libsecril-client.so')
        .add_needed('libshim_audioparams.so')
        .binary_regex_replace(b'str_parms_get_str', b'str_parms_get_mod'),
    (
    'vendor/lib/libwrappergps.so',
    'vendor/lib64/libwrappergps.so',
    ): blob_fixup()
        .replace_needed('libvndsecril-client.so', 'libsecril-client.so'),
    'vendor/lib/libaudioproxy.so': blob_fixup()
        .add_needed('libaudioproxy_shim.so'),
    (
    'vendor/lib/sensors.sensorhub.so',
    'vendor/lib64/sensors.sensorhub.so',
    ): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),
    'vendor/lib/libwvhidl.so': blob_fixup()
        .replace_needed('libprotobuf-cpp-lite.so', 'libprotobuf-cpp-lite-v29.so'),
} # fmt: skip

module = ExtractUtilsModule(
    'starlte',
    'samsung',
    namespace_imports=namespace_imports,
    blob_fixups=blob_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(module, 'exynos9810-common', module.vendor)
    utils.run()
