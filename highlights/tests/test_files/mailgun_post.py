# test contents taken from the Mailgun route tester - https://mailgun.com/cp/routes#
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

test_inbound_payload = {}
test_inbound_payload['stripped-signature']="""Thanks,
Bob"""
test_inbound_payload['From']='Bob <bob@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org>'
test_inbound_payload['attachment-count']='2'
test_inbound_payload['To']='Alice <alice@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org>'
test_inbound_payload['subject']='Re: Sample POST request'
test_inbound_payload['from']='Bob <bob@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org>'
test_inbound_payload['User-Agent']='Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20130308 Thunderbird/17.0.4'
test_inbound_payload['stripped-html']="""<html><head><meta content="text/html; charset=ISO-8859-1" http-equiv="Content-Type"></head><body text="#000000" bgcolor="#FFFFFF">
    <div class="moz-cite-prefix">
      <div style="color: rgb(34, 34, 34); font-family: arial,
        sans-serif; font-size: 12.666666984558105px; font-style: normal;
        font-variant: normal; font-weight: normal; letter-spacing:
        normal; line-height: normal; orphans: auto; text-align: start;
        text-indent: 0px; text-transform: none; white-space: normal;
        widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto;
        -webkit-text-stroke-width: 0px; background-color: rgb(255, 255,
        255);">Hi Alice,</div>
      <div style="color: rgb(34, 34, 34); font-family: arial,
        sans-serif; font-size: 12.666666984558105px; font-style: normal;
        font-variant: normal; font-weight: normal; letter-spacing:
        normal; line-height: normal; orphans: auto; text-align: start;
        text-indent: 0px; text-transform: none; white-space: normal;
        widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto;
        -webkit-text-stroke-width: 0px; background-color: rgb(255, 255,
        255);"><br></div>
      <div style="color: rgb(34, 34, 34); font-family: arial,
        sans-serif; font-size: 12.666666984558105px; font-style: normal;
        font-variant: normal; font-weight: normal; letter-spacing:
        normal; line-height: normal; orphans: auto; text-align: start;
        text-indent: 0px; text-transform: none; white-space: normal;
        widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto;
        -webkit-text-stroke-width: 0px; background-color: rgb(255, 255,
        255);">This is Bob.<span class="Apple-converted-space">&#160;<img alt="" src="cid:part1.04060802.06030207@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org" height="15" width="33"></span></div>
      <div style="color: rgb(34, 34, 34); font-family: arial,
        sans-serif; font-size: 12.666666984558105px; font-style: normal;
        font-variant: normal; font-weight: normal; letter-spacing:
        normal; line-height: normal; orphans: auto; text-align: start;
        text-indent: 0px; text-transform: none; white-space: normal;
        widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto;
        -webkit-text-stroke-width: 0px; background-color: rgb(255, 255,
        255);"><br>
        I also attached a file.<br><br></div>
      <div style="color: rgb(34, 34, 34); font-family: arial,
        sans-serif; font-size: 12.666666984558105px; font-style: normal;
        font-variant: normal; font-weight: normal; letter-spacing:
        normal; line-height: normal; orphans: auto; text-align: start;
        text-indent: 0px; text-transform: none; white-space: normal;
        widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto;
        -webkit-text-stroke-width: 0px; background-color: rgb(255, 255,
        255);">Thanks,</div>
      <div style="color: rgb(34, 34, 34); font-family: arial,
        sans-serif; font-size: 12.666666984558105px; font-style: normal;
        font-variant: normal; font-weight: normal; letter-spacing:
        normal; line-height: normal; orphans: auto; text-align: start;
        text-indent: 0px; text-transform: none; white-space: normal;
        widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto;
        -webkit-text-stroke-width: 0px; background-color: rgb(255, 255,
        255);">Bob</div>
      <br><br></div>
    <br></body></html>"""
test_inbound_payload['In-Reply-To']='<517AC78B.5060404@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org>'
test_inbound_payload['Date']='Fri, 26 Apr 2013 11:50:29 -0700'
test_inbound_payload['Message-Id']='<517ACC75.5010709@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org>'
test_inbound_payload['body-plain']="""Hi Alice,

This is Bob.

I also attached a file.

Thanks,
Bob

On 04/26/2013 11:29 AM, Alice wrote:
> Hi Bob,
>
> This is Alice. How are you doing?
>
> Thanks,
> Alice

"""
test_inbound_payload['Mime-Version']='1.0'
test_inbound_payload['Received']='from [10.20.76.69] (Unknown [50.56.129.169]) by mxa.mailgun.org with ESMTP id 517acc75.4b341f0-worker2; Fri, 26 Apr 2013 18:50:29 -0000 (UTC)'
test_inbound_payload['content-id-map']='{"<part1.04060802.06030207@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org>": "attachment-1"}'
test_inbound_payload['Sender']='bob@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org'
test_inbound_payload['timestamp']='1412239366'
test_inbound_payload['message-headers']='[["Received", "by luna.mailgun.net with SMTP mgrt 8788212249833; Fri, 26 Apr 2013 18:50:30 +0000"], ["Received", "from [10.20.76.69] (Unknown [50.56.129.169]) by mxa.mailgun.org with ESMTP id 517acc75.4b341f0-worker2; Fri, 26 Apr 2013 18:50:29 -0000 (UTC)"], ["Message-Id", "<517ACC75.5010709@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org>"], ["Date", "Fri, 26 Apr 2013 11:50:29 -0700"], ["From", "Bob <bob@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org>"], ["User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20130308 Thunderbird/17.0.4"], ["Mime-Version", "1.0"], ["To", "Alice <alice@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org>"], ["Subject", "Re: Sample POST request"], ["References", "<517AC78B.5060404@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org>"], ["In-Reply-To", "<517AC78B.5060404@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org>"], ["X-Mailgun-Variables", "{\"my_var_1\": \"Mailgun Variable #1\", \"my-var-2\": \"awesome\"}"], ["Content-Type", "multipart/mixed; boundary=\"------------020601070403020003080006\""], ["Sender", "bob@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org"]]'
test_inbound_payload['stripped-text']="""Hi Alice,

This is Bob.

I also attached a file."""
test_inbound_payload['recipient']='alice@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org'
test_inbound_payload['sender']='bob@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org'
test_inbound_payload['X-Mailgun-Variables']='{"my_var_1": "Mailgun Variable #1", "my-var-2": "awesome"}'
test_inbound_payload['token']='4166ec05b27b5d3c024252ad43df47865128c8fcde47dfea6b'
test_inbound_payload['body-html']="""<html>
  <head>
    <meta content="text/html; charset=ISO-8859-1"
      http-equiv="Content-Type">
  </head>
  <body text="#000000" bgcolor="#FFFFFF">
    <div class="moz-cite-prefix">
      <div style="color: rgb(34, 34, 34); font-family: arial,
        sans-serif; font-size: 12.666666984558105px; font-style: normal;
        font-variant: normal; font-weight: normal; letter-spacing:
        normal; line-height: normal; orphans: auto; text-align: start;
        text-indent: 0px; text-transform: none; white-space: normal;
        widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto;
        -webkit-text-stroke-width: 0px; background-color: rgb(255, 255,
        255);">Hi Alice,</div>
      <div style="color: rgb(34, 34, 34); font-family: arial,
        sans-serif; font-size: 12.666666984558105px; font-style: normal;
        font-variant: normal; font-weight: normal; letter-spacing:
        normal; line-height: normal; orphans: auto; text-align: start;
        text-indent: 0px; text-transform: none; white-space: normal;
        widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto;
        -webkit-text-stroke-width: 0px; background-color: rgb(255, 255,
        255);"><br>
      </div>
      <div style="color: rgb(34, 34, 34); font-family: arial,
        sans-serif; font-size: 12.666666984558105px; font-style: normal;
        font-variant: normal; font-weight: normal; letter-spacing:
        normal; line-height: normal; orphans: auto; text-align: start;
        text-indent: 0px; text-transform: none; white-space: normal;
        widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto;
        -webkit-text-stroke-width: 0px; background-color: rgb(255, 255,
        255);">This is Bob.<span class="Apple-converted-space">&nbsp;<img
            alt="" src="cid:part1.04060802.06030207@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org"
            height="15" width="33"></span></div>
      <div style="color: rgb(34, 34, 34); font-family: arial,
        sans-serif; font-size: 12.666666984558105px; font-style: normal;
        font-variant: normal; font-weight: normal; letter-spacing:
        normal; line-height: normal; orphans: auto; text-align: start;
        text-indent: 0px; text-transform: none; white-space: normal;
        widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto;
        -webkit-text-stroke-width: 0px; background-color: rgb(255, 255,
        255);"><br>
        I also attached a file.<br>
        <br>
      </div>
      <div style="color: rgb(34, 34, 34); font-family: arial,
        sans-serif; font-size: 12.666666984558105px; font-style: normal;
        font-variant: normal; font-weight: normal; letter-spacing:
        normal; line-height: normal; orphans: auto; text-align: start;
        text-indent: 0px; text-transform: none; white-space: normal;
        widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto;
        -webkit-text-stroke-width: 0px; background-color: rgb(255, 255,
        255);">Thanks,</div>
      <div style="color: rgb(34, 34, 34); font-family: arial,
        sans-serif; font-size: 12.666666984558105px; font-style: normal;
        font-variant: normal; font-weight: normal; letter-spacing:
        normal; line-height: normal; orphans: auto; text-align: start;
        text-indent: 0px; text-transform: none; white-space: normal;
        widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto;
        -webkit-text-stroke-width: 0px; background-color: rgb(255, 255,
        255);">Bob</div>
      <br>
      On 04/26/2013 11:29 AM, Alice wrote:<br>
    </div>
    <blockquote cite="mid:517AC78B.5060404@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org" type="cite">Hi
      Bob,
      <br>
      <br>
      This is Alice. How are you doin©?
      <br>
      <br>
      Thanks,
      <br>
      Alice
      <br>
    </blockquote>
    <br>
  </body>
</html>
"""
test_inbound_payload['References']='<517AC78B.5060404@sandbox085a3b878a964897b9b9efb2395a1f5a.mailgun.org>'
test_inbound_payload['signature']='b220bb34b816a1b00512e1a288ac9b8e5808c51de773bc13628547486eb3a80d'
test_inbound_payload['Content-Type']='multipart/mixed; boundary="------------020601070403020003080006"'
test_inbound_payload['Subject']='Re: Sample POST request'

spirit_animals_payload={}
spirit_animals_payload['Content-Type'] = 'multipart/mixed; boundary="000000000000a4afa005a8fafded'
spirit_animals_payload['Date'] = 'Fri, 26 Jun 2020 12:27:02 +0100'
spirit_animals_payload['Dkim-Signature'] = 'v=1; a=rsa-sha256; c=relaxed/relaxed;        d=gmail.com; s=20161025;        h=mime-version:references:in-reply-to:from:date:message-id:subject:to;        bh=F5nUOpXsiw9bQ5L7mh6H/P5wN47YINwyxz7WDxdWQuQ=;        b=oS3wqHP30gQk6ULpOtNEKEd9gBlVrnMVHfaseu3DmLJZYnmyLkQifpcZIoeX9jJAdq         p80wtra6kKhbjxuWOG/IggThb4Y4fIA4CAunJmtalEQ/j2aCWikZbAr5Jof+N2U3Of56         RkIe2zttmJPGaH0eBNAawD8E8LHubJRUYPjFJzv2ePYcoNS6M65KnyaJz5FGFFw7SWHC         C7Sbna5RAcuef2HQYVRFfd8eC/1FfYKrL/pVATvfs1vNcgszSy47ILWA/pL7I0IIshv/         kTH1D65uXyQeep+LJ42j7t7V7OMbYAyAtB7QPOkxnnc9tl3pVKmpb5c0GL0RXyNljzpR         Rn+A=='
spirit_animals_payload['From'] = 'Diogo Mónica <diogo.monica@gmail.com>'
spirit_animals_payload['In-Reply-To'] = '<A7257B22-5955-44D6-9DEE-C89D60D8C975@gmail.com>'
spirit_animals_payload['Message-Id'] = '<CAM_+=wvYFvUXtSqJ0KfVVfbm038_8ivd2bS9gTtsMzUwWMBBag@mail.gmail.com>'
spirit_animals_payload['Mime-Version'] = '1.0'
spirit_animals_payload['Received'] = 'by mail-pg1-f179.google.com with SMTP id p3so4836149pgh.3        for <test@sandbox637542f1ba94428daa2436b43d76e34d.mailgun.org>; Fri, 26 Jun 2020 04:27:15 -0700 (PDT)'
spirit_animals_payload['References'] = '<A7257B22-5955-44D6-9DEE-C89D60D8C975@gmail.com>'
spirit_animals_payload['Subject'] = 'iPhone Notebook export for Animal Spirits: How Human Psychology Drives the Economy, and Why It Matters for Global Capitalism (New in Paper)'
spirit_animals_payload['To'] = 'test@sandbox637542f1ba94428daa2436b43d76e34d.mailgun.org'
spirit_animals_payload['X-Envelope-From'] = 'diogo.monica@gmail.com'
spirit_animals_payload['X-Gm-Message-State'] = 'AOAM5301gbG1MsoL3XDKY5wyLRj4Mc19jd5XE3QqCyhfmcqAvO98HVe1 FcUC6g30pTtcjUGrAr6QzK/ZaJFQo5d+gKB/MM/zzIQ='
spirit_animals_payload['X-Google-Dkim-Signature'] = 'v=1; a=rsa-sha256; c=relaxed/relaxed;        d=1e100.net; s=20161025;        h=x-gm-message-state:mime-version:references:in-reply-to:from:date         :message-id:subject:to;        bh=F5nUOpXsiw9bQ5L7mh6H/P5wN47YINwyxz7WDxdWQuQ=;        b=PIOwNk346S8xDVcSgWaE51AdBjQNBMxVslqKyzm4Kh9IAZuDm9tq/mgYrMdbH86m06         YRqBkWksE1jfK/o6DS2hFEHQ0sGgV8OGM5EINBIZ3SkJiXZBwiJJBoritK6y2UO0OCWY         FP/6vRgmYYWkY3XKuJyi7baCs3B5lpCPZZ1X1fRV96EPPhsq/Jyo+9tpKxpbVc9SL++H         HF0aqZSMrWD66WBc118Eqb2pwOIlgsDcu6QTMiVc3w/7wEJ7S5KXCPMSkIZDXUXwx4/J         wyn/UAF1rzxtDpaUybRxO5tzZBOe6oIYV6wAjIbZQfQnLBVNDRAls0CmIfVb5bC78RET         sBQw=='
spirit_animals_payload['X-Google-Smtp-Source'] = 'ABdhPJz+W/NQ/xM6FkTu205g5rXQhHKR/ztpp6zGxzfY+yH0r9kXsVRv7rNG5knbDbVVoNMF/DBpjbzIkv7XRzNMKog='
spirit_animals_payload['X-Mailgun-Incoming'] = 'Yes'
spirit_animals_payload['X-Received'] = 'by 2002:a63:ec05:: with SMTP id j5mr2370233pgh.109.1593170834264; Fri, 26 Jun 2020 04:27:14 -0700 (PDT)'
spirit_animals_payload['attachment-count'] = '1'
spirit_animals_payload['body-html'] = '''<div dir="ltr"><div class="gmail_quote">Your Notebook exported from Animal Spirits: How Human Psychology Drives the Economy, and Why It Matters for Global Capitalism (New in Paper) is attached to this email.<br>
<br>
Sent from my iPhone</div><br clear="all"><div><br></div>-- <br><div dir="ltr" class="gmail_signature" data-smartmail="gmail_signature"><div dir="ltr">Diogo Mónica<br></div></div></div>
'''
spirit_animals_payload['body-plain'] = '''Your Notebook exported from Animal Spirits: How Human Psychology Drives the
Economy, and Why It Matters for Global Capitalism (New in Paper) is
attached to this email.

Sent from my iPhone
--
Diogo Mónica
'''
spirit_animals_payload['content-id-map'] = '{"<172f0612f28405e7801>": "attachment-1"}'
spirit_animals_payload['from'] = 'Diogo Mónica <diogo.monica@gmail.com>'
spirit_animals_payload['message-headers'] = '''[["X-Mailgun-Incoming", "Yes"], ["X-Envelope-From", "<diogo.monica@gmail.com>"], ["Received", "from mail-pg1-f179.google.com (mail-pg1-f179.google.com [209.85.215.179]) by mxa.mailgun.org with ESMTP id 5ef5db93.7fd09a2d1f70-api-n18; Fri, 26 Jun 2020 11:27:15 -0000 (UTC)"], ["Received", "by mail-pg1-f179.google.com with SMTP id p3so4836149pgh.3        for <test@sandbox637542f1ba94428daa2436b43d76e34d.mailgun.org>; Fri, 26 Jun 2020 04:27:15 -0700 (PDT)"], ["Dkim-Signature", "v=1; a=rsa-sha256; c=relaxed/relaxed;        d=gmail.com; s=20161025;        h=mime-version:references:in-reply-to:from:date:message-id:subject:to;        bh=F5nUOpXsiw9bQ5L7mh6H/P5wN47YINwyxz7WDxdWQuQ=;        b=oS3wqHP30gQk6ULpOtNEKEd9gBlVrnMVHfaseu3DmLJZYnmyLkQifpcZIoeX9jJAdq         p80wtra6kKhbjxuWOG/IggThb4Y4fIA4CAunJmtalEQ/j2aCWikZbAr5Jof+N2U3Of56         RkIe2zttmJPGaH0eBNAawD8E8LHubJRUYPjFJzv2ePYcoNS6M65KnyaJz5FGFFw7SWHC         C7Sbna5RAcuef2HQYVRFfd8eC/1FfYKrL/pVATvfs1vNcgszSy47ILWA/pL7I0IIshv/         kTH1D65uXyQeep+LJ42j7t7V7OMbYAyAtB7QPOkxnnc9tl3pVKmpb5c0GL0RXyNljzpR         Rn+A=="], ["X-Google-Dkim-Signature", "v=1; a=rsa-sha256; c=relaxed/relaxed;        d=1e100.net; s=20161025;        h=x-gm-message-state:mime-version:references:in-reply-to:from:date         :message-id:subject:to;        bh=F5nUOpXsiw9bQ5L7mh6H/P5wN47YINwyxz7WDxdWQuQ=;        b=PIOwNk346S8xDVcSgWaE51AdBjQNBMxVslqKyzm4Kh9IAZuDm9tq/mgYrMdbH86m06         YRqBkWksE1jfK/o6DS2hFEHQ0sGgV8OGM5EINBIZ3SkJiXZBwiJJBoritK6y2UO0OCWY         FP/6vRgmYYWkY3XKuJyi7baCs3B5lpCPZZ1X1fRV96EPPhsq/Jyo+9tpKxpbVc9SL++H         HF0aqZSMrWD66WBc118Eqb2pwOIlgsDcu6QTMiVc3w/7wEJ7S5KXCPMSkIZDXUXwx4/J         wyn/UAF1rzxtDpaUybRxO5tzZBOe6oIYV6wAjIbZQfQnLBVNDRAls0CmIfVb5bC78RET         sBQw=="], ["X-Gm-Message-State", "AOAM5301gbG1MsoL3XDKY5wyLRj4Mc19jd5XE3QqCyhfmcqAvO98HVe1\tFcUC6g30pTtcjUGrAr6QzK/ZaJFQo5d+gKB/MM/zzIQ="], ["X-Google-Smtp-Source", "ABdhPJz+W/NQ/xM6FkTu205g5rXQhHKR/ztpp6zGxzfY+yH0r9kXsVRv7rNG5knbDbVVoNMF/DBpjbzIkv7XRzNMKog="], ["X-Received", "by 2002:a63:ec05:: with SMTP id j5mr2370233pgh.109.1593170834264; Fri, 26 Jun 2020 04:27:14 -0700 (PDT)"], ["Mime-Version", "1.0"], ["References", "<A7257B22-5955-44D6-9DEE-C89D60D8C975@anchorlabs.com>"], ["In-Reply-To", "<A7257B22-5955-44D6-9DEE-C89D60D8C975@anchorlabs.com>"], ["From", "Diogo M\u00f3nica <diogo.monica@gmail.com>"], ["Date", "Fri, 26 Jun 2020 12:27:02 +0100"], ["Message-Id", "<CAM_+=wvYFvUXtSqJ0KfVVfbm038_8ivd2bS9gTtsMzUwWMBBag@mail.gmail.com>"], ["Subject", "iPhone Notebook export for Animal Spirits: How Human Psychology Drives the Economy, and Why It Matters for Global Capitalism (New in Paper)"], ["To", "test@sandbox637542f1ba94428daa2436b43d76e34d.mailgun.org"], ["Content-Type", "multipart/mixed; boundary=\"000000000000a4afa005a8fafded\""]]'''
spirit_animals_payload['recipient'] = 'test@sandbox637542f1ba94428daa2436b43d76e34d.mailgun.org'
spirit_animals_payload['sender'] = 'diogo.monica@gmail.com'
spirit_animals_payload['signature'] = 'ed21b6463b74ba565fb4f908e914882f67'
spirit_animals_payload['stripped-html'] = '''<html><head></head><body><div dir="ltr"><br clear="all"><div><br></div>-- <br><div data-smartmail="gmail_signature" class="gmail_signature" dir="ltr"><div dir="ltr">Diogo M&#3619;&#3603;nica<br></div></div></div>
</body></html>'''
spirit_animals_payload['stripped-signature'] = '''Sent from my iPhone

--
Diogo Mónica'''
spirit_animals_payload['stripped-text'] = '''Your Notebook exported from Animal Spirits: How Human Psychology Drives the
Economy, and Why It Matters for Global Capitalism (New in Paper) is
attached to this email.'''
spirit_animals_payload['subject'] = 'iPhone Notebook export for Animal Spirits: How Human Psychology Drives the Economy, and Why It Matters for Global Capitalism (New in Paper)'
spirit_animals_payload['timestamp'] = '1593170837'
spirit_animals_payload['token'] = 'ffeb3d4f884d87039bfc59e705254a5e9875d67a408cefaa35'
