#ifndef PDUR_TYPES_H
#define PDUR_TYPES_H

#include "../COM/ComStack_Types.h"
#include "PduR.h"
#include "../COM/Com.h"
#include "../CanIf/CanIf_Types.h"

/* @req PDUR324 */
/* PduR_StateType defines the states of which the PDU router can be in */
typedef enum {
	PDUR_UNINIT, /* PDU Router is not initialized. */
	PDUR_ONLINE, /* PDU Router initialized successfully. */
	PDUR_REDUCED /* PDU Router initialization did not succeed. Only minimum routing is provided. */
} PduR_StateType;

typedef struct {
	/* Link-time data configuration of PDU router, implemented in PduR_Lcfg.c */
} PduR_LConfigType;

/*		PduR structs		*/
typedef struct PduRTxBuffer {
	uint8 Length;
	uint8 Depth;
} PduRTxBuffer;

typedef struct Pdu {
	ComIPdu_type *ComPduIdRef;
	struct PduRSrcPdu *PduRSrcPduRef;
	struct PduRDestPdu *PduRDestPduRef;
	CanIf_RxPduCfgType CanIfRxPduRef;
} Pdu;

typedef struct PduRBswModule PduRBswModule;

struct PduRBswModule{
	PduRBswModule* PduRBswModuleRef;
	boolean PduRRetransmission;
	boolean PduRUseTag;
	boolean PduRTxConfirmation;
	boolean PduRCancelTransmit;
	boolean PduRCommunicationInterface;
	boolean PduRTransportProtocol;
	boolean PduRTriggertransmit;
	boolean PduRUpperModule;
	boolean PduRLowerModule;
	boolean PduRChangeParameterApi;
	boolean PduRCancelReceive;
}PduRBswModules;

typedef struct PduRGeneral {
	boolean PduRDevErrorDetect;
	boolean PduRVersionInfoApi;
	boolean PduRZeroCostOperation;
	boolean PduRMetaDataSupport;
} PduRGeneral;

typedef enum PduRDestPduDataProvision {
	PDUR_DIRECT,
	PDUR_TRIGGER_TRANSMIT
} PduRDestPduDataProvision;

struct PduRSrcPdu {
	uint16 HandleId;
	// boolean PduRSrcPduUpTxConf;
	//Pdu* SrcPduRef;
	Pdu *SrcPduRef;
};


typedef struct PduRDefaultValueElement {
	uint8 PduRDefaultValueElement;
	uint32 PduRDefaultValueElementBytePosition;
} PduRDefaultValueElement;

typedef struct PduRDefaultValue {
	PduRDefaultValueElement* PduRDefaultValueElement;
} PduRDefaultValue;

typedef struct PduRTpBuffer {
	uint32 PduRTpBufferLength;
} PduRTpBuffer;

typedef struct PduRTpBufferTable {
	uint16 PduRMaxTpBufferNumber;
	PduRTpBuffer* PduRTpBuffer;
} PduRTpBufferTable;

typedef struct PduRTxBufferTable {
	uint16 PDUR_MAX_TX_BUFFER_NUMBER;
	PduRTxBuffer* PduRTxBuffer;
} PduRTxBufferTable;

struct PduRDestPdu {
	PduRDestPduDataProvision DataProvision;
	uint16 PduRDestPduHandleId;
	uint16 PduRTpThreshold;
	boolean PduRTransmissionConfirmation;
	const Pdu* DestPduRef;
	//struct Pdu *DestPduRef;
	PduRTxBuffer* TxBufferRef;
	PduRDefaultValue PduRDefaultValue;
};

typedef struct PduRSrcPdu PduRSrcPdu;
typedef struct PduRDestPdu PduRDestPdu;

typedef struct PduRRoutingPathGroup {
	boolean PduRIsEnabledAtInit;
	uint16 PduRRoutingPathGroupId;
	PduRDestPdu *PduRDestPduRef;
} PduRRoutingPathGroup;

typedef struct PduRRoutingPath {
	uint8 SduLength;
	const PduRDestPdu * const * PduRDestPdu;
	const PduRSrcPdu * const * PduRSrcPdu;
} PduRRoutingPath;

typedef struct PduRRoutingTable {
	const PduRRoutingPath * const * PduRRoutingPath;
} PduRRoutingTable;

typedef struct PduRRoutingTables {
	uint16 PduRConfigurationId;
	uint16 PduRMaxRoutingPathCnt;
	uint16 PduRMaxRoutingPathGroupCnt;
	uint16 PduRMaxRoutingTableCnt;
	PduRRoutingPathGroup* PduRRoutingPathGroup;
	PduRRoutingTable* PduRRoutingTable;
	PduRTpBufferTable PduRTpBufferTable;
	PduRTxBufferTable PduRTxBufferTable;
} PduRRoutingTables;

typedef struct PduR_PBConfigType{
	uint16 PduR_PBConfigIdType;
	uint16 PduR_RoutingPathGroupIdType;
	PduR_StateType PduR_StateType;
	const PduRRoutingTable *RoutingTable;
} PduR_PBConfigType;
#endif