<?xml version="1.0" encoding="utf-8"?>
<EMVCoL3OnlineMessageFormat>
  <LogDetails>
    <Date-Time>2024-10-10T01:35:58.020Z</Date-Time>
    <LoggingTool>
      <ProductName>ASTREX</ProductName>
      <ProductVersion>2487</ProductVersion>
    </LoggingTool>
    <SchemaSelectionIndex>1.0</SchemaSelectionIndex>
    <L3OMLVersion>1.1</L3OMLVersion>
    <Reference>Logged by Fime ASTREX on 2024-10-10T01:35:58.020Z</Reference>
  </LogDetails>
  <ConnectionList>
    <Connection ID="{42CBCA90-18A7-4C3B-8BFA-24D3B1DE134E}">
      <Protocol>
        <FriendlyName>Visa BASE I</FriendlyName>
        <SymbolicName>VISABASEI</SymbolicName>
        <VersionInfo>2023.Q4</VersionInfo>
      </Protocol>
      <TCPIPParameters>
        <Address/>
        <Port>4323</Port>
        <Header>4 bytes, PDP Order</Header>
        <Client>false</Client>
        <Format>EBCDIC</Format>
      </TCPIPParameters>
    </Connection>
    <Connection ID="{CCE2A97D-B51C-4008-ACC4-5E971DEC382D}">
      <Protocol>
        <FriendlyName>Visa BASE I</FriendlyName>
        <SymbolicName>VISABASEI</SymbolicName>
        <VersionInfo>2023.Q4</VersionInfo>
      </Protocol>
      <TCPIPParameters>
        <Address>unknown</Address>
        <Port>4323</Port>
        <Header>4 bytes, PDP Order</Header>
        <Client>true</Client>
        <Format>EBCDIC</Format>
      </TCPIPParameters>
    </Connection>
    <Connection ID="{AA4D2A9C-F547-4720-8BD0-5D00CBCCC89A}">
      <Protocol>
        <FriendlyName>DCI Relay Xpress</FriendlyName>
        <SymbolicName>DNI</SymbolicName>
        <VersionInfo>2023.2</VersionInfo>
      </Protocol>
      <TCPIPParameters>
        <Address/>
        <Port>7003</Port>
        <Header>4 bytes, Host Order</Header>
        <Client>false</Client>
        <Format>ASCII</Format>
      </TCPIPParameters>
    </Connection>
    <Connection ID="{831543D0-69D6-48AA-81F7-34C091EB746A}">
      <Protocol>
        <FriendlyName>DCI Relay Xpress</FriendlyName>
        <SymbolicName>DNI</SymbolicName>
        <VersionInfo>2023.2</VersionInfo>
      </Protocol>
      <TCPIPParameters>
        <Address>unknown</Address>
        <Port>7003</Port>
        <Header>4 bytes, Host Order</Header>
        <Client>true</Client>
        <Format>ASCII</Format>
      </TCPIPParameters>
    </Connection>
  </ConnectionList>
  <OnlineMessageList>
 </OnlineMessageList>
  <Signature xmlns="http://www.w3.org/2000/09/xmldsig#">
    <SignedInfo>
      <CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
      <SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
      <Reference URI="">
        <Transforms>
          <Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
        </Transforms>
        <DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
        <DigestValue>eomumOjW4/M97X3BqLmn1ZfvuE8=</DigestValue>
      </Reference>
    </SignedInfo>
    <SignatureValue>C364R7e56lWFFTZW519QsSAAZ1PREa46DBY3Bgw9MDybK2sQ/rtiFEtce3Vces6uB/jyHFOpnXt6BwofeqQDYAB/Bdm0dVX+V8ozKFoMnfmpCVtdPATc1BbrNegFL/Ib+LtdCH2TX5zOms8FFRqIaEnspQcsrbaBhL9Fc929szc=</SignatureValue>
    <KeyInfo>
      <KeyName>Fime ASTREX Key 1</KeyName>
      <KeyValue>
        <RSAKeyValue>
          <Modulus>m81uEm3yhkWp+n+p0bB3ufwY/d4VjwpNXFvmkI6v6xStgmtjkWnBN7vXLwMKsg4ovxV2b4+hQ9dGDn+Yjk2Ftgp46cyYNC5MDSYJpibyiVplchFjZklHhvGBAZv3m9QjnyimMRFGJoztwWUkgKrlANklIfSISmAEdc0aB/tlQWM=</Modulus>
          <Exponent>AQAB</Exponent>
        </RSAKeyValue>
      </KeyValue>
    </KeyInfo>
  </Signature>
</EMVCoL3OnlineMessageFormat>
