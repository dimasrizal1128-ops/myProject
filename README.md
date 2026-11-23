# How to Use

1. **Initialize the Mode (Host)**
Run `import intranet` once to import library
   ```python
   import intranet
   ```
   Run `intranet.setMode(name, password)` once to create the network settings and device list.
   ```python
   intranet.setMode("MyNetwork", "12345")
   ```

3. **Set the Gateway File (Optional)**
   Use `intranet.gateaway(FileGateaway)` to set a `.txt` or `.json` file as the main data gateway, and read it with `runGate()`.
   ```python
   intranet.gateaway("gateway.txt")
   data = intranet.runGate()
   ```

4. **Connect Devices**
   Connect up to 3 devices/files to the network using `intranet.connect(nameWifi, password, NameDevices)`.
   ```python
   intranet.connect("MyNetwork", "12345", "Device1")
   intranet.connect("MyNetwork", "12345", "Device2")
   ```

5. **Pair Two Devices**
   Link two connected devices using `print(intranet.pair(name, device, targetpair)`. It will generate a secret pairing code.
   ```python
   print(intranet.pair("MyNetwork", "Device1", "Device2"))
   # Output: success!please run command runPair <code_number>
   ```

6. **Send and Read Data**
   Use the pairing code to send text data with `intranet.runpair(code, data)` and receive it from another file with `readData(code)`.
   ```python
   # Sender file
   intranet.runpair(1234, "Hello from Device1!")

   # Receiver file
   message = intranet.readData(1234)
   print(message)
   ```
