"use client";

import { useState, useEffect } from "react";
import QRCode from "react-qr-code";
import { RequestInfo } from "undici-types";

type QrResponse = {
  qr: string,
}


export default function Home() {
  const [data, setData] = useState<QrResponse>({qr: '420'});

  const getData=async ()=>{
    await fetch('https://levs57.pythonanywhere.com/get_qr', {
    mode: 'cors',
    headers: {
      'Access-Control-Allow-Origin':'*'
    }
  })
    .then(function(response){
      console.log(response);
      return response.json()
    })
    .then(function(myJson){
      console.log(myJson);
      setData(myJson)
    })
  }

  useEffect(()=>{
    getData()
  },[])

  return (
    <div className="flex flex-col justify-center items-center mt-10">
      <div className="flex w-[350px] justify-between items-center">
        <img src={"info.svg"} className="w-9" alt="info-logo" />
        <img src={"folder.svg"} className="w-9" alt="info-logo" />
        <img src={"settings.svg"} className="w-9" alt="info-logo" />
      </div>
      <div className="flex items-center bg-[#2a3231] font-sm font-light border-[#808080] border-solid rounded-xl w-[350px] p-4 py-3 justify-start mt-12 border-[1px]">
        <img src={"arrow.svg"} className="w-5 mr-3" alt="info-logo" />
        <p className="text-white">ZuConnect</p>
      </div>
      <div className="w-[350px] border-[0.5px] border-[#808080] mt-10"></div>
      <div className="w-[350px] flex justify-center border-[1px] rounded-b-none border-yellow-200 rounded-lg mt-8 border-b-0 py-2 bg-[#325F57]">
        <p className="text-center font-light text-white tracking-widest text-lg w-[80%]">
          ZUCONNECT OCTOBER-NOVEMBER &apos;23 (RESIDENT)
        </p>
      </div>
      <div className="w-[350px] mb-8 bg-white pt-10 pb-4 flex flex-col justify-center items-center border-[1px] border-yellow-200 border-t-0 rounded-t-none rounded-xl">
        <QRCode
          size={320}
          className="mx-auto"
          value={data.qr}
          //          value="zupasslengthlengthlengthlengthlengthlengthlengthlengthlengthlengthlengthlengthhlengthlenghlengthlenghlengthleng.org"
        />
        <p className="font-extralight font-xs mt-6">Lev, Rafi & Manu</p>
        <p className="font-extralight font-xs mt-2">hack@zuzalu.city</p>
        <img src="zkmode.png" alt="zk-mode" className="w-[150px] self-end mr-4" />

        <button className="bg-[#a95940] rounded-2xl text-white px-4 py-1 self-end mr-4 mt-4 font-sm">
          Remove
        </button>
      </div>
    </div>
  );
}
