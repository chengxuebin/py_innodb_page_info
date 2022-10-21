## FSP_HDR 内 encryption info -> 10390

```
6c 43 42|00 00 00 01 00  00 00 00|63 36 38 66 30  |lCB........c68f0|
34 35 31 2d 34 61 62 39  2d 31 31 65 64 2d 61 61  |451-4ab9-11ed-aa|
35 64 2d 35 32 35 34 30  30 31 65 30 36 65 62|90  |5d-5254001e06eb.|
82 60 0b 5d a9 2c df d2  c7 1d 49 1f 2c 68 f4 ee  |.`.].,....I.,h..|
45 b4 41 de fb 4e 43 59  13 5a a9 6c b4 96 15 9b  |E.A..NCY.Z.l....|
1b 8a 89 0c 6e 85 82 95  1f 13 18 64 06 b7 f4 16  |....n......d....|
6d 7c f4 6c af de cb 11  2d 35 e8 ab db 93 d5|f2  |m|.l....-5......|
01 06 c2 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
```

### 长度定义

```cpp
/** Encryption information total size for 5.7.11: magic number(3) + master_key_id(8) +
key + iv + checksum(8) = (83) */
static const ulint ENCRYPTION_INFO_SIZE_V1 = (ENCRYPTION_MAGIC_SIZE \
					 + (ENCRYPTION_KEY_LEN * 2) \
					 + 2 * sizeof(ulint));

/** Encryption information total size for 5.7.24: magic number(3) + master_key_id(4) +
key(32) + iv(32) + server_uuid(36) + checksum(4) = (119) */
static const ulint ENCRYPTION_INFO_SIZE_V2 = (ENCRYPTION_MAGIC_SIZE \
					 + (ENCRYPTION_KEY_LEN * 2) \
					 + ENCRYPTION_SERVER_UUID_LEN \
					 + 2 * sizeof(ulint));

/** Encryption information total size for 8.0.23: magic number(3) + master_key_id(4) +
key(32) + iv(32) + checksum(4) = (111) */
static constexpr size_t INFO_SIZE =
  (MAGIC_SIZE + sizeof(uint32) + (KEY_LEN * 2) + SERVER_UUID_LEN +
    sizeof(uint32));
```

### encryption 内各字段

```
magic_number:   6c4342
master_key_id:  0000000100000000
server_uuid:    63363866303435312d346162392d313165642d616135642d353235343030316530366562
tablekey:       9082600b5da92cdfd2c71d491f2c68f4ee45b441defb4e4359135aa96cb49615
iv:             9b1b8a890c6e8582951f13186406b7f4166d7cf46cafdecb112d35e8abdb93d5
checksum:       f20106c200000000
```

### 主密钥

<span style="color:red">masterkey</span>
```
a9d100fa5d754f096f2472ae28cb00f0cf3886a82b1fcdc5646d857a168769af
```

**key_name**
```shell
494e4e4f44424b65792d63363866303435312d346162392d313165642d616135642d3532353430303165303665622d31
```

### 解密表密钥和 iv

```shell
# 表密钥
ee38bc09bbb4a10b9adce9f40c739f77 e374480ca4fe661ae82c1f617ac139fb
# IV
ec9310b22819edba04402971cc722e87 747aeeb063a6d9b6f02d1adc979e5194
```
