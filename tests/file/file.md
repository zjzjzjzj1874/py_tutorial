# file操作

- 打开文件的四种模式
  - r - read (默认值)读取，打开文件进行读取，不存在则会报错
  - a - append 追加，打开供追加的读取，不存在则创建该文件
  - w - write 写入，打开文件进行写入，不存在则创建该文件
  - x - 创建，创建指定文件，如果文件存在则返回错误

- 指定文件处理模式
  - t - text (默认值)文本，文本模式
  - b - binary 二进制，二进制模式，如图像