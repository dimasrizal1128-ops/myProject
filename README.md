# How to Use

1. **Initialize the Mode (Host)**
   Run `setMode(name, password)` once to create the network settings and device list.
   ```python
   setMode("MyNetwork", "12345")
   ```

2. **Set the Gateway File (Optional)**
   Use `gateaway(FileGateaway)` to set a `.txt` or `.json` file as the main data gateway, and read it with `runGate()`.
   ```python
   gateaway("gateway.txt")
   data = runGate()
   ```

3. **Connect Devices**
   Connect up to 3 devices/files to the network using `connect(nameWifi, password, NameDevices)`.
   ```python
   connect("MyNetwork", "12345", "Device1")
   connect("MyNetwork", "12345", "Device2")
   ```

4. **Pair Two Devices**
   Link two connected devices using `pair(name, device, targetpair)`. It will generate a secret pairing code.
   ```python
   print(pair("MyNetwork", "Device1", "Device2"))
   # Output: success!please run command runPair <code_number>
   ```

5. **Send and Read Data**
   Use the pairing code to send text data with `runpair(code, data)` and receive it from another file with `readData(code)`.
   ```python
   # Sender file
   runpair(1234, "Hello from Device1!")

   # Receiver file
   message = readData(1234)
   print(message)
   ```
